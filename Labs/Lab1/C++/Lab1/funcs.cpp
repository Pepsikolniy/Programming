#include <fstream>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
using namespace httplib;

Client owm("http://api.openweathermap.org");
Client time_srv("http://worldtimeapi.org");

json cache;

void findAndReplaceAll(std::string& data, std::string toSearch, std::string replaceStr) {
    size_t pos = data.find(toSearch);
    while (pos != std::string::npos) {
        data.replace(pos, toSearch.size(), replaceStr);
        pos = data.find(toSearch, pos + replaceStr.size());
    }
}

json get_json() {
    auto res = owm.Get("/data/2.5/onecall?lat=44.952116&lon=34.102411&units=metric&exclude=current,minutely,daily,alerts&lang=ru&appid=b522dba7cc25f5d20be8b87eda9ec768");
    if (!res) {
        return ("Err");
    }
    int status = res->status;
    if (status < 200 or status >= 300) {
        return ("Err");
    }
    return json::parse(res->body);
}

json get_cache() {
    if (!cache.empty())
    {
        return cache;
    }
    json cache;
    std::ifstream cache_file("cache.json");
    if (cache_file.is_open()) {
        std::string content;
        getline(cache_file, content, '\0');

        if (!content.empty()) {
            cache = json::parse(content);
        }
        cache_file.close();
    }
    else {
        return { "err", "Could not open `cache.json` to read cache." };
    }
    return cache;
}

bool cache_json(json j) {
    cache = j;
    std::ofstream cache_file("cache.json");
    if (cache_file.is_open()) {
        cache_file << j;
        cache_file.close();
    }
    else {
        return false;
    }
    return true;
}

json get_time() {
    auto time = time_srv.Get("/api/timezone/Europe/Simferopol");
    if (!time) {
        return("Err");
        return json::object();
    }
    int status = time->status;
    if (status < 200 or status >= 300) {
        return ("Err");
    }
    return json::parse(time->body);
}

json get_hour_forecast(const json& hourly) {
    json hour_forecast;

    int last = hourly.size() - 1;
    int current_time;
    json time_j = get_time();
    if (time_j["err"].is_null()) {
        current_time = time_j["unixtime"];
    }
    else {
        current_time = std::time(0);
    }

    if (hourly[last]["dt"] < current_time) {
        return json::object();
    }

    for (int i = 0; i <= last; ++i) {
        if (hourly[i]["dt"] >= current_time) {
            hour_forecast = hourly[i];
            break;
        }
    }
    return hour_forecast;
}