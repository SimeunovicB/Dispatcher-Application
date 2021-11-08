const authModule = {
    // namespaced: true,
    state: {
        authenticated: false,
        administrator: false,
        id: null
    },
    mutations: {
        SET_AUTH: (state, auth) => state.authenticated = auth,
        SET_ADMIN: (state, admin) => state.administrator = admin,
        SET_ID: (state, id) => state.id = id
    },
    actions: {
        setAuth: ({ commit }, auth) => commit('SET_AUTH', auth), //commit
        setAdmin: ({ commit }, admin) => commit('SET_ADMIN', admin),
        setId: ({ commit }, id) => commit('SET_ID', id)
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
        }
    }
}

export default authModule;