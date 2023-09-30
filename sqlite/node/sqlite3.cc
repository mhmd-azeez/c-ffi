#include <napi.h>
#include <sqlite3.h>

#define OK 0

Napi::Number ExecSql(const Napi::CallbackInfo &info) {
  Napi::Env env = info.Env();

  if (info.Length() < 2 || !info[0].IsExternal() || !info[1].IsString()) {
    Napi::TypeError::New(env, "Invalid arguments. Expected: Exec(connection, sql)").ThrowAsJavaScriptException();
    return Napi::Number::New(env, -1);
  }

  sqlite3* connection = info[0].As<Napi::External<sqlite3>>().Data();
  std::string sql = info[1].As<Napi::String>().Utf8Value();

  char* errMsg = nullptr;

  int result = sqlite3_exec(connection, sql.c_str(), nullptr, nullptr, &errMsg);

  if (result != OK) {
    Napi::Error::New(env, std::string("Error Code: ") + std::to_string(result) + ". Message: " + errMsg).ThrowAsJavaScriptException();
    return Napi::Number::New(env, result);
  }

  return Napi::Number::New(env, result);
}

Napi::Value Open(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();

  if (info.Length() < 1 || !info[0].IsString()) {
    Napi::TypeError::New(env, "Path to the database file must be provided as a string").ThrowAsJavaScriptException();
    return env.Null();
  }

  std::string path = info[0].As<Napi::String>().Utf8Value();
  sqlite3* connection;

  int result = sqlite3_open(path.c_str(), &connection);

  if (result != OK) {
    const char* message = sqlite3_errmsg(connection);
    Napi::Error::New(env, std::string("Failed to open DB: ") + message).ThrowAsJavaScriptException();
    return env.Null();
  }

  return Napi::External<sqlite3>::New(env, connection);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports["exec"] = Napi::Function::New(env, ExecSql);
  exports["open"] = Napi::Function::New(env, Open);
  return exports;
}

NODE_API_MODULE(sqlite, Init)


