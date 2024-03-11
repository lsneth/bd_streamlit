import streamlit as st
import polars as pl
import altair as alt

df = pl.read_parquet('./data/survey_results_public.parquet')

def show_explore_page():
    st.title('Explore Page')

    st.header('Stack Overflow Developer Survey Data')
    st.dataframe(df.head())

    test = df\
        .drop_nulls(subset=['YearsCode', 'YearsCodePro', 'ConvertedCompYearly'])\
        .with_columns(
            pl.col('YearsCode').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
            pl.col('YearsCodePro').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
        )\
        .with_columns((pl.col('YearsCode') - pl.col('YearsCodePro')).alias('YearsCodeNonPro'))\
        .select(pl.col('YearsCode'), pl.col('YearsCodePro'), pl.col('YearsCodeNonPro'), pl.col('ConvertedCompYearly'))\
        .filter(pl.col('YearsCodeNonPro') > 0)\
        .filter(pl.col('YearsCodePro') > 0)\
        .filter(pl.col('YearsCode') > 0)\
        .sort('YearsCodePro')
        
    st.header('Developer Count By Number of Years of Professional Experience')
    st.line_chart(test.group_by('YearsCodePro').count(), x='YearsCodePro', y='count')

    st.header('Salary of 10 Year Pros by Number of Nonpro Years of Experience')
    st.scatter_chart(test.filter(pl.col('YearsCodePro') == 10), x='ConvertedCompYearly', y='YearsCodeNonPro', size=5)

    st.header('Salary of 4 Year Pros by Number of Nonpro Years of Experience')
    st.scatter_chart(test.filter(pl.col('YearsCodePro') == 4), x='ConvertedCompYearly', y='YearsCodeNonPro', size=5)
    
    chart = alt.Chart(test.filter(pl.col('YearsCodePro') == 4)).mark_circle(size=5).encode(
        x=alt.X('ConvertedCompYearly', scale=alt.Scale(domain=(0, 200000))),
        y=alt.Y('YearsCodeNonPro', scale=alt.Scale(domain=(0, 10))),
        tooltip=['ConvertedCompYearly', 'YearsCodeNonPro']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)