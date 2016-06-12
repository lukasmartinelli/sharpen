import collections


def length_longest_substring(text):
    longest_substring = 0
    i = 0

    while i < len(text):
        unique_chars = collections.OrderedDict()
        original_i = i

        for j in range(i, len(text)):
            to_char = text[j]
            if to_char in unique_chars:
                i = j
                break
            else:
                unique_chars[to_char] = j
                i += 1

        for j in reversed(range(0, original_i)):
            to_char = text[j]
            if to_char in unique_chars:
                break
            else:
                unique_chars[to_char] = j

        print(original_i, unique_chars.keys())
        longest_substring = max(longest_substring, len(unique_chars))

    return longest_substring

    """
    for i, from_char in enumerate(text):
        unique_chars = {}

        for j, to_char in enumerate(text[i:]):
            if to_char in unique_chars:
                longest_substring = max(longest_substring, len(unique_chars))
                break
            else:
                unique_chars[to_char] = j

        # After last run choose max again
        longest_substring = max(longest_substring, len(unique_chars))
    """

    return longest_substring


def test_length_longest_substring():
    assert length_longest_substring("dadbc") == 4
    assert length_longest_substring("") == 0
    assert length_longest_substring("u") == 1
    assert length_longest_substring("bbbbb") == 1
    assert length_longest_substring("abcabcbb") == 3
    assert length_longest_substring("acbcadf") == 5
    assert length_longest_substring("abcadcb") == 4


def test_long_substring():
    text = "bj520A9rdOqd1BHpRoir0BbLGBUU6xBuvlUj689jB3WxfNyL8jvku9qLbQUqpeTNGLs5Xmi03yWmbOk5xBnKcaEnEOmYcPt5TZCSRSaH42r050LBt6BRdveb8jKNqfLZHdjupnMIuZlfKz8Bn5HWj1lnLMCCFWnWqCVnDOH1DlJsy5VFx5rsuipiByhQLmghSGGPSYaB5xzx9Qu5KSuBqrVsn0CUuikDuhwnTSpyuioE1idgge1BYPH0JdnMLyiHpUr5OOrRHX4xgwaViGkR72OKLYCTtyHlKXPs6AY6aerGxuXhHf7cn3b2ruDodmjLXIM9F1lt5O2wbPB21sqRZ6OidBDNVNFS4HsbwmhnUudapmcEWKZtksHIGKv7vkzPMzaMiIth8qgIXSz8pK6L1AzCZ5EJGFXtMaLPNrm2vRFM0cVrpZyGN3MC31bP4PTKBSeceRQMOfJVfSopZ2e7dkdg1z6VPylwwsSLX6zrJMtpzvHgvMmxwrwiYAeHWKRfimWY5wndT9JnULO6UxWICN6C2sqdtWm98ivGAemSI6tI47KqGT1ZlcX6RJiqfdFUxWs03NEgezyLpal0awkBIv61mcJBMBFULqJe270Ayk3Fd4cGLrZaHnko06tj2ZMkPx5O2QbL0vFiWzx7RaM7JLAjoQCtvHni7q3zXxOngDfSYXNFYwOHTWPBPAc3R6oegEbuKhDEMTPVDiDiCcgEocCel3eYFGC34PkjCNDSdVusYvLjUXLsYtmnavD0WEJS1rkVx0t2CgRNe2sRvtxWv9VlsTT25ytJPuddPJhVPQUR9WSlnzaMediEhkgOzmklAaveIld5VouLfaB3TwLeostw0CEhO6CLXmF1ZpQxmxXSft8RdacVnEJzBMeATecTBKDByQClQAPUutdFkSCWmt2BdXq4Q7xfAIsjKyLhclUcnoKuyctNpbMvOEqbCrLwEIfBFPdxQ3BvR0kxh8E2zCueGD1db1XHJrQwuqIPr9zJa6KbYd0rKy2M1abok2ClaoZLQD3vYqgtgGesBr2tyCM1PGufdUurcDA7D00t9H6PwhKSEu52OEvJLksXUTtON715MaZmL6f9vbdGaZfffLD0WL2KxU5rs7LM0s3qhc6QLGPk7jzvHvXlWckxvdawX0P9S5yHmVvH7IED9UHHLN0OVCubqUvSPZiHsPftBDQcU6Sr9z5XHBnO6FN2V2c9zvPMwmSYS9qh4hmAcKeoMS8iHXip3w7GnzwElTlA93hBG26DjrgRDZbsQ0IcnY7iIx8bcytSn2eJlaluqJW6u7ztM2nN75JGWmtTYsqqYQFxd6lJHWNaPMY8GDhAR46B7V98iyPzoiO8KVc1viI7qY4DTwoHaciVmEo5xU1yOB0D0UOKdr3Hf1zwUbfW21NQb2Stp8w5qaTOX562ZdjJdKlcfgt4nlR4dhy3pQFneeJWRXScIdAlkNj7Ix5RN71CEUEcPkNLQcO3GDD8MF9UehWoEQ7dAuofqgtmPUMPpW0mXrj67Bfr4RgZ6UQp838XKcRujzajWkrNKMIdFv6OLTeEg7JH2skrrulYVn5DftBXxwWzn8RXDWpj1QNf3PqqSSvnYIrtLyudsrjNZe0lRPMycMfWrPsJw6GPvw5hhPpkRn5Av90XQc5DL5wKwRBbmNqf0kk9RHypofNUGCNu713O"
    assert length_longest_substring(text) == 30
