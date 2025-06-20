def pytest_tavern_beta_after_test_run(test_dict, test_case, response):
    if "quote" in response.json():
        assert isinstance(response.json()["quote"], str)
