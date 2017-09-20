
# coding: utf-8

# In[*]

import pandas as pd

data = './suicides.csv'
df = pd.read_csv(data)
print(df.head())


# In[*]

df.describe()


# Lets see for which states do we have the data.

# In[*]

# Groupby states
df_state = df.drop('Year', axis=1)
df_state = df_state.groupby('State', as_index=False).agg({'Total': 'sum'})
print(df_state.head())


# In[*]

print('Dropping the non relevant fields')
print('Shape before dropping the fields {}'.format(df_state.shape))

df_state = df_state.drop(df_state.index[df_state.State == 'Total (All India)'])
df_state = df_state.drop(df_state.index[df_state.State == 'Total (States)'])
df_state = df_state.drop(df_state.index[df_state.State == 'Total (Uts)'])

print('Shape after dropping the fields {}'.format(df_state.shape))


# In[*]

print('Changing to jsonstr to feed to html file')
jsonstr = df_state.to_json(orient='records')

print(jsonstr)

# Display the Dive visualization for this data
from IPython.core.display import display, HTML

HTML_TEMPLATE = """<link rel="import" href="/nbextensions/facets-dist/facets-jupyter.html">
        <facets-dive id="elem" height="600"></facets-dive>
        <script>
          var data = {jsonstr};
          document.querySelector("#elem").data = data;
        </script>"""
html = HTML_TEMPLATE.format(jsonstr=jsonstr)
out = HTML(html).data

# write the html to a file
with open('html_file.html', 'w') as f:
    f.write(out)
print('file saved')

