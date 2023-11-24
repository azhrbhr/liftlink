<template>
    <div class="container mt-5">
        <!-- Hero Section -->
        <div class="row align-items-center">
            <div class="col-lg-12">
                <h1 class="display-4">Welcome to LiftLink</h1>
                <p class="lead">Your trusted platform for ridesharing and carpooling.</p>
                <router-link to="/rides" class="btn btn-primary btn-lg">Find a Ride</router-link>
            </div>
        </div>

        <!-- How It Works Section -->
        <section class="mt-5">
            <h2 class="text-center mb-4">How LiftLink Works</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="text-center mb-3">
                        <i class="bi bi-search h1 text-primary"></i>
                    </div>
                    <h5 class="text-center">Find Rides</h5>
                    <p class="text-center">Discover available rides based on your destination.</p>
                </div>
                <div class="col-md-4">
                    <div class="text-center mb-3">
                        <i class="bi bi-person h1 text-primary"></i>
                    </div>
                    <h5 class="text-center">Connect with Drivers</h5>
                    <p class="text-center">Connect with drivers offering rides along your route.</p>
                </div>
                <div class="col-md-4">
                    <div class="text-center mb-3">
                        <i class="bi bi-check2 h1 text-primary"></i>
                    </div>
                    <h5 class="text-center">Enjoy the Journey</h5>
                    <p class="text-center">Enjoy a comfortable and cost-effective journey with LiftLink.</p>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <!-- Add a section with user testimonials if needed -->

        <!-- CTA Section -->
        <section class="mt-5 bg-light p-4 text-center">
            <h2>Ready to get started?</h2>
            <p class="lead">Join LiftLink today and experience the convenience of ridesharing.</p>
            <router-link to="/register" class="btn btn-primary btn-lg">Sign Up</router-link>
        </section>
    </div>
</template>
  
<script lang="ts" setup>
</script>
  
<style scoped>
/* Add custom styles for this component if needed */
</style>
  