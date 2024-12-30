<template>
  <div id="app">
    <StudentForm />
  </div>
</template>

<script>
import StudentForm from './components/StudentForm.vue';

export default {
  components: {
    StudentForm
  }
};
</script>

<style>
/* Global styles can go here */
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
  padding: 20px;
}
</style>