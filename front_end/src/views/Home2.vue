<template>
    <Sender/>
</template>

<script>
// @ is an alias to /src
import Sender from '@/components/Sender.vue'
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'Home2',
    components: {
        HelloWorld,
        Sender
    },
    methods:{
      onPress: function(){
          console.log(this.$route.params.cookie)
      }
    }
}
</script>
