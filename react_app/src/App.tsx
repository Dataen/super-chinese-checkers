import React from 'react';
import { Typography, Grid, Container, makeStyles } from '@material-ui/core'
import Board from './components/Board';
import ControlPanel from './components/ControlPanel';

const useStyles = makeStyles({

});

function App() {

  const classes = useStyles();

  return (
    <Grid
      container
      direction="row"
      justify="center"
      spacing={1}
    >
      <Grid item xs={8}>
        <Board />
      </Grid>
      <Grid item xs={4}>
        <ControlPanel />
      </Grid>
    </Grid>
  );
}

export default App;
