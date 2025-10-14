import { createContext, useContext, useReducer, useEffect } from 'react'
import { toast } from 'react-toastify'
import api from '../services/api'

const AppContext = createContext()

const initialState = {
  user: null,
  token: localStorage.getItem('token'),
  events: [],
  clubs: [],
  loading: false,
  error: null
}

function appReducer(state, action) {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, loading: action.payload }
    case 'SET_ERROR':
      return { ...state, error: action.payload, loading: false }
    case 'LOGIN_SUCCESS':
      localStorage.setItem('token', action.payload.token)
      return {
        ...state,
        user: action.payload.user,
        token: action.payload.token,
        error: null
      }
    case 'LOGOUT':
      localStorage.removeItem('token')
      return {
        ...state,
        user: null,
        token: null,
        events: [],
        clubs: []
      }
    case 'SET_EVENTS':
      return { ...state, events: action.payload }
    case 'ADD_EVENT':
      return { ...state, events: [...state.events, action.payload] }
    case 'UPDATE_EVENT':
      return {
        ...state,
        events: state.events.map(event =>
          event.id === action.payload.id ? action.payload : event
        )
      }
    case 'SET_CLUBS':
      return { ...state, clubs: action.payload }
    case 'ADD_CLUB':
      return { ...state, clubs: [...state.clubs, action.payload] }
    case 'UPDATE_CLUB':
      return {
        ...state,
        clubs: state.clubs.map(club =>
          club.id === action.payload.id ? action.payload : club
        )
      }
    default:
      return state
  }
}

export function AppProvider({ children }) {
  const [state, dispatch] = useReducer(appReducer, initialState)

  // Initialize user from token on app start
  useEffect(() => {
    const initializeUser = async () => {
      if (state.token) {
        try {
          const response = await api.get('/auth/me')
          dispatch({
            type: 'LOGIN_SUCCESS',
            payload: { user: response.data.data, token: state.token }
          })
        } catch (error) {
          dispatch({ type: 'LOGOUT' })
        }
      }
    }
    initializeUser()
  }, [])

  const login = async (credentials) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true })
      const response = await api.post('/auth/login', credentials)
      dispatch({ type: 'LOGIN_SUCCESS', payload: response.data.data })
      toast.success('Login successful!')
      return { success: true }
    } catch (error) {
      const message = error.response?.data?.message || 'Login failed'
      dispatch({ type: 'SET_ERROR', payload: message })
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const register = async (userData) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true })
      const response = await api.post('/auth/register', userData)
      dispatch({ type: 'LOGIN_SUCCESS', payload: response.data.data })
      toast.success('Registration successful!')
      return { success: true }
    } catch (error) {
      const message = error.response?.data?.message || 'Registration failed'
      dispatch({ type: 'SET_ERROR', payload: message })
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const logout = () => {
    dispatch({ type: 'LOGOUT' })
    toast.info('Logged out successfully')
  }

  const fetchEvents = async (params = {}) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true })
      const response = await api.get('/events', { params })
      dispatch({ type: 'SET_EVENTS', payload: response.data.data.events })
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: 'Failed to fetch events' })
    }
  }

  const createEvent = async (eventData) => {
    try {
      const response = await api.post('/events', eventData)
      dispatch({ type: 'ADD_EVENT', payload: response.data.data })
      toast.success('Event created successfully!')
      return { success: true, data: response.data.data }
    } catch (error) {
      const message = error.response?.data?.message || 'Failed to create event'
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const rsvpEvent = async (eventId, status) => {
    try {
      await api.post(`/events/${eventId}/rsvp`, { status })
      toast.success(`RSVP updated to ${status}!`)
      // Refresh events to get updated registration count
      fetchEvents()
      return { success: true }
    } catch (error) {
      const message = error.response?.data?.message || 'RSVP failed'
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const fetchClubs = async (params = {}) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true })
      const response = await api.get('/clubs', { params })
      dispatch({ type: 'SET_CLUBS', payload: response.data.data.clubs })
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: 'Failed to fetch clubs' })
    }
  }

  const createClub = async (clubData) => {
    try {
      const response = await api.post('/clubs', clubData)
      dispatch({ type: 'ADD_CLUB', payload: response.data.data })
      toast.success('Club created successfully!')
      return { success: true, data: response.data.data }
    } catch (error) {
      const message = error.response?.data?.message || 'Failed to create club'
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const joinClub = async (clubId) => {
    try {
      await api.post(`/clubs/${clubId}/join`)
      toast.success('Successfully joined club!')
      // Refresh clubs to get updated member count
      fetchClubs()
      return { success: true }
    } catch (error) {
      const message = error.response?.data?.message || 'Failed to join club'
      toast.error(message)
      return { success: false, error: message }
    }
  }

  const value = {
    ...state,
    login,
    register,
    logout,
    fetchEvents,
    createEvent,
    rsvpEvent,
    fetchClubs,
    createClub,
    joinClub
  }

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>
}

export const useApp = () => {
  const context = useContext(AppContext)
  if (!context) {
    throw new Error('useApp must be used within an AppProvider')
  }
  return context
}