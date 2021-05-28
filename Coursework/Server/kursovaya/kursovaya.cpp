#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

#include "include/httplib.h"
#include "include/json.hpp"

using namespace httplib;
using namespace std;
using json = nlohmann::json;

void entry(const Request& req, Response& res)
{
    json JSON;
    JSON = json::parse(req.body);
    cout << req.body << endl;
    ifstream input("users.json");

    if (input.is_open())
    {
        cout << "JSON file opened" << endl;
    }
    else
        cout << "can't open JSON file" << endl;
    json j;
    input >> j;
    input.close();

    for (auto& user : j) {
        if (user["login"] == JSON["login"] && user["password"] == JSON["password"])
        {
            res.set_content("Logged in", "text/plain");
            cout << "Logged in" << endl;
            return;
        }
        else
        {
            cout << "Incorrect input" << endl;
            res.set_content("Incorrect input", "text/plain");
        }
        cout << user["login"] << '\t' << user["password"] << endl;
    }

}

void registration(const Request& req, Response& res)
{
    json JSON;
    JSON = json::parse(req.body);
    cout << req.body << endl;
    ifstream input("users.json");

    if (input.is_open())
    {
        cout << "JSON file opened" << endl;
    }
    else
        cout << "can't open JSON file" << endl;
    json j;
    input >> j;
    input.close();

    bool have_same = false;
    for (auto& user : j) {
        if (user["login"] == JSON["login"])
        {
            res.set_content("This user already exists", "text/plain");
            cout << "This user already exists" << endl;
            have_same = true;
        }
        cout << JSON["login"] << '\t' << JSON["password"] << endl;
    }
    if (!have_same)
    {
        j.push_back(
            {
                {"login", JSON["login"]},
                {"password", JSON["password"]},
                {"games", 1},
                {"bestScore", 1}
            }
        );
        cout << "You have successfully registered an account" << endl;
        res.set_content("You have successfully registered an account", "text/plain");
    }

    ofstream users("users.json");
    users << setw(2) << j << endl;
    users.close();
}

void games(const Request& req, Response& res)
{
    json player;
    player = json::parse(req.body);
    ifstream input("users.json");

    if (input.is_open())
    {
        cout << "JSON file opened" << endl;
    }
    else
        cout << "can't open JSON file" << endl;
    json us;
    input >> us;
    input.close();

    for (auto& user : us) {
        if (user["login"] == player["login"] && user["password"] == player["password"])
        {
            cout << '1';
            user["games"] = user["games"].get<int>() + 1;
            cout << user["login"] << " games +1\t";
            res.set_content("Games +1", "text/plain");
            if (player["bestScore"].get<int>() > user["bestScore"].get<int>())
            {
                user["bestScore"] = player["bestScore"];
                cout << user["login"] << " New best score: " << user["bestScore"] << endl;
                res.set_content("New best score", "text/plain");
            }
        }
    }

    ofstream use("users.json");
    use << setw(2) << us << endl;
    use.close();
}

void rating(const Request& req, Response& res)
{
    json JSON;
    JSON = json::parse(req.body);
    cout << req.body << endl;
    ifstream input("users.json");

    if (input.is_open())
    {
        cout << "JSON file opened" << endl;
    }
    else
        cout << "can't open JSON file" << endl;
    json j;
    input >> j;
    input.close();

    json temp;
    for (int i = 0; i < j.size() - 1; i++)
    {
        for (int k = 0; k < j.size() - i - 1; k++)
        {
            if (j[k]["bestScore"].get<int>() < j[k + 1]["bestScore"].get<int>())
            {
                temp = j[k];
                j[k] = j[k + 1];
                j[k + 1] = temp;
            }
        }
    }

    cout << setw(2) << j;
    int index;
    for (int i = 0; i < j.size(); i++)
    {
        if (JSON["login"] == j[i]["login"])
        {
            index = i;
        }
    }
    json rating;
    rating.push_back(j[0]);
    rating.push_back(j[1]);
    rating.push_back(j[2]);
    rating.push_back(j[3]);
    rating.push_back(j[4]);
    rating.push_back(
        {
            {"login", j[index]["login"]},
            {"password", j[index]["password"]},
            {"games", j[index]["games"]},
            {"bestScore", j[index]["bestScore"]},
            {"place", index+1}
        });
    res.set_content(rating.dump(2), "text/plain");
}

int main()
{
    setlocale(LC_ALL, "Russian");

    Server srv;

    srv.set_exception_handler([](const Request&, Response& res, std::exception& e) {
        cout << "Exception: " << e.what() << endl;
        json j{ {"status", "server-error"} };
        res.set_content(j.dump(), "text/plain;charset=utf-8");
        });

    srv.Post("/entry", entry);
    srv.Post("/registration", registration);
    srv.Post("/games", games);
    srv.Post("/rating", rating);

    cout << "Start server... OK\n";
    srv.listen("localhost", 5000);
}
