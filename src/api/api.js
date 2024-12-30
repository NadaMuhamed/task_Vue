const BASE_URL = 'http://localhost:8000/api/resource'; // Adjust this if necessary

export const registerStudent = async (student) => {
  const response = await fetch(`${BASE_URL}/Student Registration`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(student),
  });

  if (!response.ok) {
    const errorResponse = await response.json();
    throw new Error(errorResponse.message || 'Network response was not ok');
  }

  return response.json();
};