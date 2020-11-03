test = {
  'name': 'Question 3_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # michelle_sample_size should be Michelle's sample size!
          >>> michelle_sample_size == 9975
          True
          >>> # smaller_sample_size should be smaller than Michelle's sample size!
          >>> smaller_sample_size < michelle_sample_size
          True
          >>> # larger_sample_size should be larger than Michelle's sample size!
          >>> larger_sample_size > michelle_sample_size
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(michelle_sample_mean_sd, 0.005000)
          True
          >>> smaller_sample_mean_sd > michelle_sample_mean_sd
          True
          >>> larger_sample_mean_sd < michelle_sample_mean_sd
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
