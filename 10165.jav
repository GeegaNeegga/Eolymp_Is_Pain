 

long long powmod(long long x, long long n, long long m)

{

if (n == 0) return 1;

if (n % 2 == 0) return powmod((x * x) % m, n / 2, m);

return (x * powmod(x, n - 1, m)) % m;

}

 


 

scanf("%lld", &n);

 


 

if (n == 1) res = 1;

else res = powmod(2, n - 2, 123456789);

printf("%lld\n", res);