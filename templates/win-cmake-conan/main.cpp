#include <iostream>
#include <format>

#include <entt/entt.hpp>

struct Position {
    float x;
    float y;
};

std::ostream& operator << (std::ostream& os, const Position& pos)
{
    return os << std::format("(x:{}, y:{})", pos.x, pos.y);
}

struct Velocity {
    float dx;
    float dy;
};

std::ostream& operator << (std::ostream& os, const Velocity& vel)
{
    return os << std::format("(dx:{}, dy:{})", vel.dx, vel.dy);
}

void update(entt::registry &registry) {
    auto view = registry.view<const Position, Velocity>();

    // use a callback
    view.each([](const auto &pos, auto &vel) {
        std::cout << "pos = " << pos << " vel = " << vel << std::endl;
    });

    // use an extended callback
    view.each([](const auto entity, const auto &pos, auto &vel) { /* ... */ });

    // use a range-for
    for(auto [entity, pos, vel]: view.each()) {
        // ...
    }

    // use forward iterators and get only the components of interest
    for(auto entity: view) {
        auto &vel = view.get<Velocity>(entity);
        // ...
    }
}

int main() {
    entt::registry registry;

    for(auto i = 0u; i < 10u; ++i) {
        const auto entity = registry.create();
        registry.emplace<Position>(entity, i * 1.f, i * 1.f);
        if(i % 2 == 0) { registry.emplace<Velocity>(entity, i * .1f, i * .1f); }
    }

    update(registry);
}
