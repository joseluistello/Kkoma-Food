<template>
  <div id="wrapper">


    <nav class="navbar is-light">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Kkoma</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="¿Que es lo que buscas?" name="query">
                </div>

                <div class="control">
                  <button class="button is-info">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">

          
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Más departamentos
            </a>

            <div class="navbar-dropdown">
              <router-link to="/bebidas" class="navbar-item">
                Bebidas
              </router-link>  

              <router-link to="/farmacia" class="navbar-item">
                Farmacia
              </router-link>


              <router-link to="/mascota" class="navbar-item">
                Mascotas
              </router-link>

            </div>
          </div>
          

          <router-link to="/frutasyverduras" class="navbar-item">Frutas y verduras</router-link>
          <router-link to="" class="navbar-item"></router-link>
          <router-link to="/carnesypescados" class="navbar-item">Carnes y Pescados</router-link>
          <router-link to="" class="navbar-item"></router-link>
          <router-link to="/lacteosyhuevo" class="navbar-item">Lácteos y Huevo</router-link>
          <router-link to="" class="navbar-item"></router-link>
          <router-link to="/granel" class="navbar-item">Granel</router-link>

          <div class="navbar-item">
            <div class="buttons">

              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-dark">Mi cuenta</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-dark">Iniciar Sesion</router-link>
              </template>

              <router-link to="/cart" class="button is-info">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span> {{ cartTotalLength }}</span>
              </router-link>
              
            </div>
          </div>

        </div>


      </div>
    </nav>







    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>






    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Kkoma</strong> by <a href="https://joseluistello.live/">José Luis Tello</a>.
        </p>
      </div>
    </footer>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initialzeStore')

    const token = this.$store.state.token
    
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>



<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
