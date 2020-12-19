#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace httplib;

json get_webhooks();
void save_webhooks(json config);
std::string gen_webhook_page();
void webhooks_post(const Request& req, Response& res);

const std::string config_file_name = "config.json";
const std::string webpage_file_name = "webhooks.html";
const std::string webhook_template = u8R"(
                    <div class="form-row align-items-center">
                      <div class="col">
                        <input type="text" value="{Webhook URL}" class="form-control mb-2" disabled>
                      </div>
                      <div class="col">
                        <button type="submit" name="del" value="{Webhook URL}" class="btn btn-danger mb-2">Удалить</button>
                      </div>
                    </div>)";

void findAndReplaceAll(std::string& data, std::string toSearch, std::string replaceStr)
{
	size_t pos = data.find(toSearch);
	while (pos != std::string::npos)
	{
		data.replace(pos, toSearch.size(), replaceStr);
		pos = data.find(toSearch, pos + replaceStr.size());
	}
}
json get_webhooks()
{
	std::ifstream config_file(config_file_name);
	json config;

	if (config_file.is_open())
	{
		config_file >> config;
		config_file.close();
	}

	return config;
}
void save_webhooks(json config)
{
	std::ofstream config_file(config_file_name);

	if (config_file.is_open())
	{
		config_file << config.dump(4);
		config_file.close();
	}
	else
	{
		std::cout << "Ошибка пути или прав доступа" << std::endl;
	}
}

std::string gen_webhook_page()
{
	std::ifstream webpage_file(webpage_file_name);
	std::string webpage;
	if (webpage_file.is_open())
	{
		std::getline(webpage_file, webpage, '\0');
		webpage_file.close();
	}

	else return "";
	json config = get_webhooks();
	if (!config["webhooks"].empty()) {
		for (auto weebs : config["webhooks"]) {
			int baran = webpage.find("{webhooks_list}") - 1;
			std::string templ = webhook_template;
			findAndReplaceAll(templ, "{Webhook URL}", weebs.get<std::string>());
			webpage.insert(webpage.begin() + baran, templ.begin(), templ.end());
		}
	}
	findAndReplaceAll(webpage, "{webhooks_list}", "");
	return webpage;
}

void webhooks_get(const Request& req, Response& res)
{
	res.set_content(gen_webhook_page(), "text/html; charset=UTF-8");
}

void webhooks_post(const Request& req, Response& res)
{
	json config = get_webhooks();
	if (req.has_param("del"))
	{
		std::string value = req.get_param_value("del");
		if (!config["webhooks"].empty())
		{
			for (auto ptr = config["webhooks"].begin(); ptr != config["webhooks"].end(); ++ptr)
			{
				if (ptr->is_string() && ptr->get<std::string>() == value)
				{
					config["webhooks"].erase(ptr);
					break;
				}
			}
		}
	}
	else if (req.has_param("set"))
	{
		std::string value = req.get_param_value("set");

		if (value == "")
		{
		}
		else
		{
			if (!config["webhooks"].empty())
			{
				bool found = false;
				for (auto ptr = config["webhooks"].begin(); ptr != config["webhooks"].end(); ++ptr)
				{
					if (ptr->is_string() && ptr->get<std::string>() == value)
					{
						found = true;
					}
				}
				if (!found) {
					config["webhooks"].push_back(value);
				}
			}
			else
			{
				config["webhooks"].push_back(value);
			}
		}
	}
	save_webhooks(config);
	res.set_content(gen_webhook_page(), "text/html; charset=UTF-8");
	std::cout << std::endl;
}