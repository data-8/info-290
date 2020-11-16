test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your estimate should be positive, and should also not be absurdly large
          >>> 0 < eth_predictor(10) < 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(eth_predictor(25), 3.397726922655913)
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
