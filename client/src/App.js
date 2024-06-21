import React, {useState, useEffect} from 'react'

export default function App() {

  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const handleClick = () => {

    fetch('/insert-user', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: formData.username,
        email: formData.email,
        password: formData.password
      }),
    })
    .then(response => response.json())
    .then(data => {
      alert("Data inserted!")
      setData(data)
      formData.username = ""
      formData.email = ""
      formData.password = ""
    });


  }

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };
  const [data, setData] = useState([{}])

  useEffect(() => {

      fetch("/employees").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
        }
      )

  }, [])




  return (
    <>
      <div>
        <label >Email: </label>
        <input type='email' name='email' placeholder='Email' onChange={handleChange} value={formData.email} /> <br />

        <label >Username: </label>
        <input type='text' name='username' placeholder='Username' onChange={handleChange} value={formData.username} /> <br />

        <label >Password: </label>
        <input type='password' name='password' placeholder='Password' onChange={handleChange} value={formData.password} /> <br />

        <button onClick={handleClick}> Send </button>

        <br />
        <br />

        <table >
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Password</th>
            </tr>
          </thead>
          <tbody>
            {
              data.map(function(e, i) {
                return (
                  <tr key={i}>
                    <td>{e.username}</td>
                    <td>{e.email}</td>
                    <td>{e.password}</td>
                  </tr>
                )
              })
            }
          </tbody>
        </table>

      </div>
    </>

  )
}


