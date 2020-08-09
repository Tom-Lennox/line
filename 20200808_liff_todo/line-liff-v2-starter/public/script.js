'use strict'

const app = new Vue({
    el: '#app',
    data: {
        displayName: '',
        userId: '',
        statusMessage: '',
        pictureUrl: '',
        profile: '',
        getOS: '',
    },
    methods: {
        getProfile: async function(){
            const accessToken = liff.getAccessToken()
            const profile = await liff.getProfile()
            this.getOS = liff.getOS()
            this.profile = profile
            // ## ▼ profile
            // displayName
            // userId
            // pictureUrl
            // statusMessage
        },
        logout: async function(){
            if (liff.isLoggedIn()){
                console.log('logout()')
                liff.logout()
                window.location.reload()
            }
        },
    },
    mounted: async function(){
        await liff.init({
            liffId: '1654657286-jvor2EQb'
        })
        if(liff.isInClient()){
            console.log('in LINE')
            this.getProfile()
        }else{
            if(liff.isLoggedIn()){
                console.log('not LINE')
                this.getProfile()
            }else{
                liff.login()
            }
        }
    }
})
