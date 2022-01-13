<template>
    <div id="messages" v-for="message in messages" class="container mt-3 bt-margin">
        <Message :message="message"/>
    </div>
    <nav class="navbar fixed-bottom navbar-light bg-light d-flex justify-content-center">
        <div class="d-flex flex-row">
            <input type="text" class="form-control me-2" placeholder="Type here" v-model="payload.user_message" @keyup.enter.native="sendData">
            <button class="btn btn-primary sendBtn" @click="sendData"><i class="bi bi-send-fill"></i></button>
        </div>
    </nav>
</template>

<script>
    // Component imports
    import Message from './Message.vue'
    import Api from '../apis/api.js'

    // Class definition:
    const api = new Api();

    export default {
        name: 'Sender',
        components:{
            Message
        },
        data(){
            return {
                messages:[],
                payload: {}
            }
        },
        methods: {
            sendData:function (){
                if (this.payload.user_message === undefined) return
                this.messages.push({
                    text: this.payload.user_message,
                    user: true
                })
                api.post(this.payload)
                .then( response => {
                    this.messages.push(response.data)
                });
                this.payload.user_message = undefined;
                window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
            }
        },
        mounted(){
            console.log(this.$route.params.cookie)
        }
        
    }
</script>

<style>
    .sendBtn {
        border-radius: 50%;
    }

    .bt-margin {
      margin-bottom: 70px !important;
    }
</style>
