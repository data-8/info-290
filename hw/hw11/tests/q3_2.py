test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Ensure your correlation function returns one number between -1 and 1
          >>> abs(correlation(Table().with_columns('a', np.random.normal(0, 1, 10),'b', np.random.normal(0, 1, 10)))) <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(standard_units(d.column(0)).item(2), 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(correlation(d), -0.5272196186749782)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
