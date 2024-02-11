% Задание 1

x = linspace(-6,6); % предел
y = x.^2; % график

y1 = x-2;
y2 = abs(x)-2;
y3 = (abs(x)-2)-3;

subplot(2,2,1)
plot(x,y)
xlabel('f(x) = x^2')
grid on;

subplot(2,2,2)
plot(x,y1)
xlabel('f(x) = x-2')
grid on;

subplot(2,2,3)
plot(x,y2)
xlabel('f(x) = |x|-2')
grid on;

subplot(2,2,4)
plot(x,y3)
xlabel('f(x) = (|x|-2)-3')
grid on;

xlim([-7 7]); % пределы отображения
ylim([-40 40]);