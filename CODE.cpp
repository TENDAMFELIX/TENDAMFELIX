- 👋 Hi, I’m @TENDAMFELIX
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
TENDAMFELIX/TENDAMFELIX is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll N;
    cin >> N;
    vector<ll> VEC(N);
    map<ll, ll> MAP;
    map<ll, ll> MAP2;
    for (int i = 0; i < N; i++)
    {
        cin >> VEC[i];
        MAP[VEC[i]]++;
        MAP2[VEC[i]] = i + 1;
    }
    sort(VEC.begin(), VEC.end());
    MAP[VEC[0]] == 1 ? cout << MAP2[VEC[0]] << endl : cout << "Still Rozdil" << endl;
}
