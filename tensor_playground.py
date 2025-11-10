import torch
print("\n--- 1) Criando tensores basicos ---")

t1 = torch.tensor([1.0, 2.0, 3.0])

print("t1:", t1)
print("shape:", t1.shape)

t2 = torch.tensor(
    [
      [1.0, 2.0],
      [3.0, 4.0]  
    ]
)
print("\nt2:\n", t2)
print("shape:", t2.shape)

t3 = torch.randn(3, 3)
print("\nt3:\n", t3)

print("\n--- 2) Operacoes basicas ---")

a = torch.tensor([10.0, 20.0, 30.0])
b = torch.tensor([1.0,2.0,3.0])

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("\n--- Broadcasting ---")

M = torch.tensor([[1.0,2.0,3.0]])
v = torch.tensor([10.0, 20.0, 30.0])
print("M + v\n", M + v)

print("\n--- 4) Produto Matricial ---")

m1 = torch.randn(2,3)
m2 = torch.randn(3,4)
print("m1 @ m2 shape:", (m1 @ m2).shape)

print("\n--- 5) Mudanca de forma (reshape) ---")
x = torch.arange(12)
print("x:", x)
print("x reshape (3,4):\n", x.reshape(3,4))

print("\n--- 6) Expandindo e reduzindo dimensoes ---")
y = torch.tensor([1.0, 2.0, 3.0])
print("original:", y, y.shape)

print("unsqueeze (adiciona dimensao):", y.unsqueeze(0), y.unsqueeze(0).shape)
print("unsqueeze (1):", y.unsqueeze(1), y.unsqueeze(1).shape)
z = torch.tensor([[1.0,2.0,3.0]])
print("squeeze:", z, z.squeeze(), z.squeeze().shape)

print("\n--- 7) Conexao com NumPy ---")
x_np = x.numpy()
print("x_np:", x_np, type(x_np))
x_back = torch.from_numpy(x_np)

print("x_back", x_back, type(x_back))

print("\n Fim do modulo de tensores!")