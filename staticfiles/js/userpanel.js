class WelcomeUser extends React.Component {
	render() {
		return (
			<h1>Welcomer {{this.props.userName}}</h1>
		);
	}
}

ReactDOM.render(
	<div>
		<WelcomeUser userName=user />
	</div>,
	document.querySelector('#container')
);