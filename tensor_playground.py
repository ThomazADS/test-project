import torch
# print("\n--- 1) Criando tensores basicos ---")

# t1 = torch.tensor([1.0, 2.0, 3.0])

# print("t1:", t1)
# print("shape:", t1.shape)

# t2 = torch.tensor(
#     [
#       [1.0, 2.0],
#       [3.0, 4.0]  
#     ]
# )
# print("\nt2:\n", t2)
# print("shape:", t2.shape)

# t3 = torch.randn(3, 3)
# print("\nt3:\n", t3)

# print("\n--- 2) Operacoes basicas ---")

# a = torch.tensor([10.0, 20.0, 30.0])
# b = torch.tensor([1.0,2.0,3.0])

# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)

# print("\n--- Broadcasting ---")

# M = torch.tensor([[1.0,2.0,3.0]])
# v = torch.tensor([10.0, 20.0, 30.0])
# print("M + v\n", M + v)

# print("\n--- 4) Produto Matricial ---")

# m1 = torch.randn(2,3)
# m2 = torch.randn(3,4)
# print("m1 @ m2 shape:", (m1 @ m2).shape)

# print("\n--- 5) Mudanca de forma (reshape) ---")
# x = torch.arange(12)
# print("x:", x)
# print("x reshape (3,4):\n", x.reshape(3,4))

# print("\n--- 6) Expandindo e reduzindo dimensoes ---")
# y = torch.tensor([1.0, 2.0, 3.0])
# print("original:", y, y.shape)

# print("unsqueeze (adiciona dimensao):", y.unsqueeze(0), y.unsqueeze(0).shape)
# print("unsqueeze (1):", y.unsqueeze(1), y.unsqueeze(1).shape)
# z = torch.tensor([[1.0,2.0,3.0]])
# print("squeeze:", z, z.squeeze(), z.squeeze().shape)

# print("\n--- 7) Conexao com NumPy ---")
# x_np = x.numpy()
# print("x_np:", x_np, type(x_np))
# x_back = torch.from_numpy(x_np)

# print("x_back", x_back, type(x_back))

# print("\nEstatistics\nMedia de m1: ", m1.mean())
# print("\nDesvio padrao de m1: ", m1.std())

# print("\nTransposicao de m1:")
# print("\nm1 = ", m1, "Transposta: ", m1.T)


# print("\n Fim do modulo de tensores!")

# x = torch.tensor([2.0], requires_grad=True)

# y = 3*x**2 + 2*x + 1

# print("x = ", x.item())
# print("y = ", y.item())

# y.backward()

# print("dy/dx = ", x.grad.item())

x = torch.linspace(0, 10, 100).unsqueeze(1)
y = 2*x + 1 + 0.5*torch.randn_like(x)

w = torch.randn(1, requires_grad = True)
b = torch.randn(1, requires_grad = True)

lr = 0.01

for epoch in range(300):

    y_pred = w * x + b

    loss = torch.mean((y_pred - y) ** 2)

    if w.grad is not None:
        w.grad.zero_()
        b.grad.zero_()

    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    if epoch % 50 == 0:
        print(f"Epoca {epoch:03d} | Loss: {loss.item():.4f} | w: {w.item():.3f} | b: {b.item():.3f}")

print("\nTreinamento finalizado!")
print(f"Parametro final: w = {w.item():.3f}, b = {b.item():.3f}")