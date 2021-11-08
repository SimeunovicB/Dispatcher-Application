import { createStore } from 'vuex'

export default createStore({
    state: {
        authenticated: false,
        administrator: false,
        id: null,
        leads: null,
    },
    mutations: {
        SET_AUTH: (state, auth) => state.authenticated = auth,
        SET_ADMIN: (state, admin) => state.administrator = admin,
        SET_ID: (state, id) => state.id = id,
        SET_LEADS: (state, leads) => state.leads = leads,
    },
    actions: {
        setAuth: ({ commit }, auth) => commit('SET_AUTH', auth), //commit
        setAdmin: ({ commit }, admin) => commit('SET_ADMIN', admin),
        setId: ({ commit }, id) => commit('SET_ID', id),
        setLeads: ({ commit }, leads) => commit('SET_LEADS', leads),
    },
    getters: {
        loggedIn(state) {
            return state.authenticated;
        },
        isAdmin(state) {
            return state.administrator;
        },
        getId(state) {
            return state.id;
        },
        getLeads(state) {
            return state.leads;
        }
    },
    modules: {

    }
})


// import { createStore } from 'vuex'
// import authModule from './modules/auth'

// export default createStore({
//     modules: {
//         auth: authModule
//     }
// }) 