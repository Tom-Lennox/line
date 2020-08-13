<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <!-- <v-card>
        <v-card-title class="headline">
          Welcome to the Vuetify + Nuxt.js template
        </v-card-title>
        <v-card-text>
          <p>
            Vuetify is a progressive Material Design component framework for
            Vue.js. It was designed to empower developers to create amazing
            applications.
          </p>
          <p>
            For more information on Vuetify, check out the
            <a
              href="https://vuetifyjs.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              documentation </a
            >.
          </p>
          <p>
            If you have questions, please join the official
            <a
              href="https://chat.vuetifyjs.com/"
              target="_blank"
              rel="noopener noreferrer"
              title="chat"
            >
              discord </a
            >.
          </p>
          <p>
            Find a bug? Report it on the github
            <a
              href="https://github.com/vuetifyjs/vuetify/issues"
              target="_blank"
              rel="noopener noreferrer"
              title="contribute"
            >
              issue board </a
            >.
          </p>
          <p>
            Thank you for developing with Vuetify and I look forward to bringing
            more exciting features in the future.
          </p>
          <div class="text-xs-right">
            <em><small>&mdash; John Leider</small></em>
          </div>
          <hr class="my-3" />
          <a
            href="https://nuxtjs.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Nuxt Documentation
          </a>
          <br />
          <a
            href="https://github.com/nuxt/nuxt.js"
            target="_blank"
            rel="noopener noreferrer"
          >
            Nuxt GitHub
          </a>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" nuxt to="/inspire">
            Continue
          </v-btn>
        </v-card-actions>
      </v-card> -->
    </v-flex>
    <v-flex xs12 sm8 md6>
      <section class="container">
        <p class="line-id">LINE ID：{{ lineId }}</p>
        <pre>{{ $data }}</pre>
        <div class="form">
          <div class="control">
            <input
              v-model="formData.name"
              class="input"
              type="text"
              placeholder="お名前"
            />
          </div>
          <button class="button is-info is-fullwidth" @click="onSubmit()">
            送信する
          </button>
          <button class="button is-light is-fullwidth" @click="handleCancel()">
            キャンセル
          </button>
        </div>
      </section>
    </v-flex>
  </v-layout>
</template>

<script>
import liff from '@line/liff'
liff.init({ liffId: '1654657286-jvor2EQb' })

export default {
  data() {
    return {
      formData: {
        name: '',
      },
      lineId: null,
      profile: '',
      getOS: '',
    }
  },
  mounted() {
    liff.login()
    console.log('liff.isLoggedIn()', liff.isLoggedIn())
    console.log('liff.getOS()', liff.getOS())
    console.log('liff.getLanguage()', liff.getLanguage())
    console.log('liff.getVersion()', liff.getVersion())
    console.log('liff.isInClient()', liff.isInClient())
    console.log('liff.isLoggedIn()', liff.isLoggedIn())
    console.log('liff.getOS()', liff.getOS())
    console.log('liff.getLineVersion()', liff.getLineVersion())
  },
  methods: {
    onSubmit() {
      if (!this.canUseLIFF()) {
        return
      }

      liff
        .sendMessages([
          {
            type: 'text',
            text: `お名前：\n${this.formData.name}`,
          },
          {
            type: 'text',
            text: '送信が完了しました',
          },
        ])
        .then(() => {
          liff.closeWindow()
        })
        .catch((e) => {
          window.alert('Error sending message: ' + e)
        })
    },
    handleCancel() {
      if (!this.canUseLIFF()) {
        return
      }
      liff.closeWindow()
    },
    canUseLIFF() {
      return navigator.userAgent.includes('Line') && liff
    },
  },
}
</script>
