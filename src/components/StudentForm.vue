<template>
  <div class="form-container">
    <h1>Student Registration</h1>
    <form @submit.prevent="submitForm" class="student-form">
      <div class="form-group">
        <label for="name">Student Name:</label>
        <input type="text" v-model="student.name" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="student.email" required />
      </div>
      <div class="form-group">
        <label for="course">Course Interest:</label>
        <select v-model="student.course" required>
          <option disabled value="">Select a course</option>
          <option>Web Development</option>
          <option>Mobile Development</option>
          <option>Data Science</option>
        </select>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number:</label>
        <input type="text" v-model="student.phone" required />
      </div>
      <div class="form-group">
        <label for="start_date">Expected Start Date:</label>
        <input type="date" v-model="student.start_date" required />
      </div>
      <button type="submit" :disabled="loading" class="submit-button">Submit</button>
      <div v-if="loading" class="loading">Loading...</div>
      <div v-if="message" class="message">{{ message }}</div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { registerStudent } from '../api/api'; // Adjusted path

export default {
  setup() {
    const student = ref({
      name: '',
      email: '',
      course: '',
      phone: '',
      start_date: ''
    });
    const loading = ref(false);
    const message = ref('');

    const submitForm = async () => {
      loading.value = true;
      message.value = '';

      try {
        await registerStudent(student.value); // Call the API service
        message.value = 'Registration Successful!';
        Object.keys(student.value).forEach(key => student.value[key] = ''); // Clear form
      } catch (error) {
        message.value = `Error: ${error.message}`;
      } finally {
        loading.value = false;
      }
    };

    return {
      student,
      loading,
      message,
      submitForm
    };
  }
};
</script>

<style scoped>
.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  text-align: center;
}

h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 30px;
}

.student-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

label {
  margin-bottom: 8px;
  font-weight: bold;
  color: #555;
}

input, select {
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
  transition: all 0.3s ease;
  box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
}

input:focus, select:focus {
  border-color: #007BFF;
  outline: none;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.5);
}

.submit-button {
  padding: 12px;
  background-color: #FF6F20;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
  font-weight: bold;
}

.submit-button:hover {
  background-color: #e65c00;
}

.submit-button:disabled {
  background-color: #ccc;
}

.loading, .message {
  margin-top: 10px;
  text-align: center;
  color: #333;
  font-size: 16px;
}

.message {
  color: #28a745;
}

.error {
  color: #dc3545;
}

@media (max-width: 768px) {
  .form-container {
    padding: 30px;
  }

  h1 {
    font-size: 22px;
  }

  input, select, .submit-button {
    font-size: 16px;
  }
}
</style>