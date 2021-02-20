import React from 'react';
import { Typography, Grid } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';
import { IHex } from './interfaces';

const useStyles = makeStyles({
});

function HexComponent({
  hex
 }: {
    hex: IHex
  }) {

  const classes = useStyles();

  const colors = (player: number) => {
    const cols = ['red', 'yellow', 'blue', 'green', 'purple', 'pink']
    return cols[player - 1]
  }

  return (
    <div className={"hex"} style={{ background: colors(hex.piece) }}>
      {hex.id}
    </div>
  );
}

export default HexComponent;
