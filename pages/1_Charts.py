import streamlit as st
import polars as pl
import altair as alt

st.set_page_config(page_title="Charts")

st.title('[Charts](https://docs.streamlit.io/library/api-reference/charts)')

st.header('Stack Overflow Developer Survey Data')

@st.cache_data
def get_survey_data():
    return pl.read_parquet('./data/survey_results_public.parquet')\
            .drop_nulls(subset=['YearsCodePro', 'ConvertedCompYearly'])\
            .with_columns(
                pl.col('YearsCode').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
                pl.col('YearsCodePro').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
            )\
            .sort('YearsCodePro')

df = get_survey_data()

st.dataframe(df.head())

st.header('Salary by Number of Years of Professional Experience - [`st.scatter_chart`](https://docs.streamlit.io/library/api-reference/charts/st.scatter_chart)')
st.scatter_chart(df, x='YearsCodePro', y='ConvertedCompYearly', size=5)

st.header('Salary by Number of Years of Professional Experience - [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)')
chart = alt.Chart(df).mark_circle(size=5).encode(
    x='YearsCodePro',
    y=alt.Y('ConvertedCompYearly', scale=alt.Scale(domain=(0, 300000))),
    tooltip=['YearsCodePro', 'ConvertedCompYearly']
).interactive()
st.altair_chart(chart, use_container_width=True)

st.write('''
---
         
### Altair Wrappers
- `st.area_chart`
- `st.bar_chart`
- `st.line_chart`
- `st.scatter_chart`
         
### Library Integrations
- `st.pyplot`
- `st.altair_chart`
- `st.vega_lite_chart`
- `st.plotly_chart`
- `st.bokeh_chart`
- `st.pydeck_chart`
- `st.graphviz_chart`
- `st.map`
''')