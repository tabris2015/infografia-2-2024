extends CharacterBody2D

var is_attacking = false
@onready var player = $AnimationPlayer

func _ready() -> void:
	player.play("Idle")
	
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		player.play("Attack")
		is_attacking = true

	if not is_attacking:
		player.play("Idle")

func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	is_attacking = false
