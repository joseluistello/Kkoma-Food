<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">¡Gracias!</h1>

                <p>Tu orden estara lista en 24 horas</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = ' Kkoma '
    },
}
</script>