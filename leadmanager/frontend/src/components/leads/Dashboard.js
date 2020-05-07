import React, { Fragment } from 'react'
import Form from './Form';
import Leads from './Leads';

// functional component to display form and leads class
export default function Dashboard() {
    return (
        <Fragment>
            <Form />
            <Leads />
        </Fragment>
    )
}
