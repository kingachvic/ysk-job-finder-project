import React from 'react';
import axios from 'axios';

class  Jobs extends React.Component{
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
	
	render(){return(
		<div className = "jobs">
			<h6>current jobs in your place</h6>
			<div className = "places">
				{this.state.jobs.map(job => <h6>{job.place}</h6>)}
			</div>
		</div>
	);
	}
}

export default Jobs;