# fleet-service-maker
A starting point for building versioned fleet unit files. Uses python and jinja templates under the hood.

## Usage

This is intended to be used in a build pipeline to create versioned fleet services.
You would ideally fork a private copy of this, adding your template files to the
`script` folder as necessary. Assuming docker access, this is how you would use the
service to build version 1.7 of the sample template provided:

    % docker build -t "fleet-service-maker" .
    % docker run -i fleet-service-maker python script/make-service.py sample 1.7 > my-template-v1.7.service
