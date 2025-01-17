import React from 'react';
import {Routes,Route} from 'react-router-dom';
import Header from './header';
import MainContent from './mainContent';
import Login from './login';
import UploadImage from './uploadimage';
import UploadDescription from './uploadDescription';
import Signin from './signin';


const HomePage = () =>{

   

    return(
        <div>
            <Header />
            <Routes>
                <Route path='/' element={<MainContent/>}/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/uploadimage' element={<UploadImage/>}/>
                <Route path='/uploaddescription' element={<UploadDescription/>}/>
                <Route path='/signin' element={<Signin/>}/>
            </Routes>
        </div>
    )
}

export default HomePage;