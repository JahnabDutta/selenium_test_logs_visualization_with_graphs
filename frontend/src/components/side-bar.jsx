import React , { Component } from 'react';
import {Drawer,IconButton } from '@mui/material';
// import themeprovider

import {useTheme} from '@mui/styles';
import { makeStyles } from '@mui/styles';
import MenuIcon from '@mui/icons-material/Menu';
import HomeIcon from '@mui/icons-material/Home';
import SettingsIcon from '@mui/icons-material/Settings';
import InfoIcon from '@mui/icons-material/Info';




function SideBar(){
    
    return(
        <Drawer 
        variant="permanent" 
        anchor="left"
        classes = {{
            paper: "drawerPaper"

        }}
        >
            <IconButton>
                <MenuIcon />
            </IconButton>
            <IconButton>
                <HomeIcon />
            </IconButton>
            <IconButton>
                <SettingsIcon/>
            </IconButton>
            <IconButton>
                <InfoIcon/>
            </IconButton>
        </Drawer>
    )
}

export default SideBar;