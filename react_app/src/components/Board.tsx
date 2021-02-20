import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Paper } from '@material-ui/core';
import HexComponent from './HexComponent';
import { IBoard } from './interfaces';

const useStyles = makeStyles({
    board: {
        background: "#FFFFFF",
    },
});

function Board() {
    const classes = useStyles();
    const [hexes, setHexes] = useState<IBoard>({ board: [] });
    const [loading, setLoading] = useState(false);

    async function fetchData() {
        const res = await fetch("http://localhost:5000/getnewboard");
        res
            .json()
            .then(res => setHexes(res))
            .then(() => setLoading(false))
            .catch(err => console.log(err));
    }
    useEffect(() => {
        setLoading(true);
        fetchData();
    }, []);

    return (
        <Paper className={classes.board} elevation={3}>
            {hexes.board.map((hex, i) => <HexComponent key={hex.id} hex={hex} />)}
        </Paper>
    );
}

export default Board;
