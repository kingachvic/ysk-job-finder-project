import React, {useState} from 'react';
import Button from '@material-ui/core/Button'
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import TextField from '@material-ui/core/TextField'
import FormHelperText from '@material-ui/core/FormHelperText'
import FormControl from '@material-ui/core/FormControl'
import Radio from '@material-ui/core/Radio'
import Checkbox from '@material-ui/core/Checkbox'
import RadioGroup from '@material-ui/core/RadioGroup'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import { Link } from 'react-router-dom'
import axios from 'axios';

class Hello extends React.Component {
	
	constructor(){
		super();
		this.state={
			jobs : []
		};
	}
	
	fetchData(){
		axios.get('http://localhost:8000/api/jobs')
		.then(res => {
			this.setState({
				jobs:res.data});
			console.log(res.data);
		});
	}

	componentDidMount(){
		this.fetchData();
	}

	render() {
		return(
			<Grid container spacing={1}>
				<Grid item xs={12} align="center">
					<Typography component='h4' variant='h4'>
						Welcome to Jobfinder!!
					</Typography>
				</Grid>
				<Grid item sm={12} align="center" position="fixed">
					<FormControl>
						<TextField required = {true} type = "text" inputProps = {{ style:{textAlign:"left"}}}></TextField>
						<FormHelperText><div>input destination</div></FormHelperText>
					</FormControl>
				</Grid>
				<Grid item xs={12} align="center">
					<Button color='primary' variant='contained' to = '/jobs' component={Link} >Submit</Button>
				</Grid>
			</Grid>
			
	);

	}


}



export default Hello; 