<script>
export default {
    data() {
        return{

        }
    },
    method:{
        logout()
    {
        let LoginForm=document.getElementById('LoginForm');
        let formdata= new FormData(LoginForm);
        fetch("/api/auth/logout",{
            method:'POST',
            body:formdata,
            headers:{
                  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
                }
        })
        .then(function (response) 
        {
            return response.json();
        })
        .then(function (data)
         {
         // display a success message
            console.log(data);
        })
        .catch(function (error) 
        {
            console.log(error);
        });
    },

    }
}
</script>