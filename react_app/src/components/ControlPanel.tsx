import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Paper } from '@material-ui/core';


const useStyles = makeStyles({
    panel: {
        background: "#FFFFFF",
    },
});

function ControlPanel() {

    const classes = useStyles();

    return (
        <Paper className={classes.panel} elevation={3}>
            Content
        </Paper>
    );
}

export default ControlPanel;
