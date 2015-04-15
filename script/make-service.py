from jinja2 import FileSystemLoader, Environment
import argparse
import os

parser = argparse.ArgumentParser(description='Create a fleet service from a template.')
parser.add_argument('template',
                    type=str,
                    help='template name')
parser.add_argument('tag',
                    type=str,
                    help='Docker Image Tag',
                    default='latest')

args = parser.parse_args()


# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
#
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
templateLoader = FileSystemLoader( searchpath=os.path.dirname(__file__) )

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = Environment( loader=templateLoader )

# This constant string specifies the template file we will use.
service_template = args.template + ".jinja"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( service_template )

# Specify any input variables to the template as a dictionary.
templateVars = { "tag" : args.tag }

# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

print(outputText)
