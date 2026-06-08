#!/usr/bin/env python3
"""Basic tests for game logic without GUI"""

from characters import Player, Enemy

def test_character_creation():
    """Test that characters are created with proper health"""
    player = Player(100)
    enemy = Enemy(100)
    
    assert player.health == 100, f"Player health should be 100, got {player.health}"
    assert enemy.health == 100, f"Enemy health should be 100, got {enemy.health}"
    print("✓ Character creation test passed")

def test_attack():
    """Test that attack reduces health"""
    player = Player(100)
    enemy = Enemy(100)
    
    initial_health = enemy.health
    damage = player.attack(enemy)
    
    assert damage >= 5 and damage <= 15, f"Damage should be 5-15, got {damage}"
    assert enemy.health < initial_health, "Enemy health should decrease after attack"
    assert enemy.health == initial_health - damage, "Health should decrease by exact damage amount"
    print("✓ Attack test passed")

def test_heal():
    """Test that healing increases health"""
    player = Player(50)
    
    initial_health = player.health
    healed = player.heal(player)
    
    assert healed >= 1 and healed <= 10, f"Healed amount should be 1-10, got {healed}"
    assert player.health > initial_health, "Player health should increase after heal"
    assert player.health == min(100, initial_health + healed), "Health should increase correctly"
    print("✓ Heal test passed")

def test_health_boundaries():
    """Test that health stays within 0-100 bounds"""
    player = Player(100)
    enemy = Enemy(100)
    
    # Test max health cap
    player.increase_health(50)
    assert player.health == 100, "Health should cap at 100"
    
    # Test min health floor
    enemy.decrease_health(200)
    assert enemy.health == 0, "Health should floor at 0"
    print("✓ Health boundaries test passed")

def test_inventory():
    """Test player inventory management"""
    player = Player()
    
    assert not player.has_item("key"), "Player should not have key initially"
    
    player.get_key()
    assert player.has_item("key"), "Player should have key after get_key()"
    
    player.pickup_gun()
    assert player.has_item("gun"), "Player should have gun after pickup_gun()"
    assert player.has_gun, "Player.has_gun should be True"
    print("✓ Inventory test passed")

def test_broken_legs():
    """Test broken legs mechanics"""
    player = Player(100)
    
    assert not player.broken_legs, "Player should not have broken legs initially"
    
    player.break_legs()
    assert player.broken_legs, "Player should have broken legs after break_legs()"
    
    player.heal_legs()
    assert not player.broken_legs, "Player legs should be healed"
    print("✓ Broken legs test passed")

if __name__ == "__main__":
    test_character_creation()
    test_attack()
    test_heal()
    test_health_boundaries()
    test_inventory()
    test_broken_legs()
    print("\n✅ All tests passed!")
