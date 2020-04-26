import React, { Component } from "react";
import { GoogleLogin } from "react-google-login";
import styled from 'styled-components';

class Login extends Component {

    constructor(props) {
        super(props);
        this.state = {
            id: '',
            name: '',
            provider: '',
        }
    }

    responseGoogle = (res) => {
        console.log(res)
    }

    resposneFail = (err) => {
        console.error(err);
    }

    render () {
        return (
            <Container>
                <GoogleLogin 
                    clientId= '918500591677-ppbhdcpu07o9d36g21ckkrqrqs55s61b.apps.googleusercontent.com'
                    buttonText="Login"
                    onSuccess={this.responseGoogle}
                    onFailure={this.resposneFail}
                />
            </Container>
        )
    }
}

const Container = styled.div`
    display: flex;
    flex-flow: column wrap;
`

export default Login;