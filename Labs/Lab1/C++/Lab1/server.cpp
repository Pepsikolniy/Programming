#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <ctime>

#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp>
#include "funcs1.h"

using json = nlohmann::json;
using namespace httplib;

void response(const Request& req, Response& res)
{
    json hour_forecast;
    json body;

    body = get_cache();
    if (body.empty())
    {
        body = get_json();
        if (!body["err"].is_null())
        {
            res.set_content(body["err"], "text/plain;charset=utf-8");
            return;
        }
        cache_json(body);
    }
    else if (!body["err"].is_null())
    {
        res.set_content(body, "text/json;charset=utf-8");
    }
    hour_forecast = get_hour_forecast(body["hourly"]);

    std::ifstream template_file("template.html");
    std::string site;
    getline(template_file, site, '\0');
    template_file.close();

    findAndReplaceAll(site, "{hourly[i].weather[0].description}",
        hour_forecast["weather"][0]["description"]);
    findAndReplaceAll(site, "{hourly[i].weather[0].icon}",
        hour_forecast["weather"][0]["icon"]);
    findAndReplaceAll(site, "{hourly[i].temp}",
        std::to_string(int(std::round(hour_forecast["temp"].get<double>()))));

    res.set_content(site, "text/html;charset=utf-8");
}

void responseraw(const Request& req, Response& res) {
    json hour_forecast;
    json body;
    body = get_cache();
    if (body.empty())
    {
        body = get_json();
        if (!body["err"].is_null())
        {
            res.set_content(body, "text/json;charset=utf-8");
            return;
        }
    }
    else if (!body["err"].is_null())
    {
        res.set_content(body, "text/json;charset=utf-8");
    }
    hour_forecast = get_hour_forecast(body["hourly"]);

    std::ifstream template_file("template.html");
    std::string site;
    getline(template_file, site, '\0');
    template_file.close();
    json out;
    out["temp"] = hour_forecast["temp"];
    out["description"] = hour_forecast["weather"][0]["description"];

    res.set_content(out.dump(), "text/json;charset=utf-8");
}

int main() {
    Server svr;
    svr.Get("/", response);
    svr.Get("/raw", responseraw);
    svr.listen("localhost", 3000);
}