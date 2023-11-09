from django.contrib.gis.db import models
import uuid

# class FenceGate(models.Model):
# 	id = models.PositiveIntegerField(primary_key=True)
# 	name = models.CharField(blank=True, null=True)

# 	def __str__(self) -> str:
# 		return f"{self.id} : {self.name}"


# class BuildingGate(models.Model):
# 	id = models.PositiveIntegerField(primary_key=True)
# 	name = models.CharField(blank=True, null=True)

# 	def __str__(self) -> str:
# 		return f"{self.id} : {self.name}"
function_list = (
	('E', 'Electric'),
	('A', 'Automatic'),
	('M', 'Manual')
)

type_list = (
	('V', 'Vehicle Access'),
	('F', 'Footpath Access'),
	('L', 'Lamb Creep'),
	('S', 'Step-Over')
)

material_list = (
	('B', 'Barbed Wire'),
	('C', 'Chain-Link'),
	('F', 'Field Fence'),
	('R', 'Wood Rail'),
	('I', 'Wrought Iron')
)

class GateFunction(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	uuid = models.UUIDField(default = uuid.uuid4)
	last_update = models.DateTimeField(auto_now=True)
	last_update_by = models.CharField(blank=True, null=True)
	primary_function = models.CharField(
		max_length=1,
		blank=True,
		null=True,
		choices=function_list
	)
	notes = models.CharField(blank=True, null=True)
	image = models.CharField(blank=True, null=True)

	def __str__(self) -> str:
		return f"{self.id} : {self.get_primary_function_display()}"


class GateType(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	uuid = models.UUIDField(default = uuid.uuid4)
	last_update = models.DateTimeField(auto_now=True)
	last_update_by = models.CharField(blank=True, null=True)
	primary_type = models.CharField(
		max_length=1,
		blank=True,
		null=True,
		choices=type_list
	)
	notes = models.CharField(blank=True, null=True)
	image = models.CharField(blank=True, null=True)

	def __str__(self) -> str:
		return f"{self.id} : {self.get_primary_type_display()}"


class GateMaterial(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	uuid = models.UUIDField(default = uuid.uuid4)
	last_update = models.DateTimeField(auto_now=True)
	last_update_by = models.CharField(blank=True, null=True)
	material = models.CharField(
		max_length=1,
		blank=True,
		null=True,
		choices=material_list
	)
	notes = models.CharField(blank=True, null=True)
	image = models.CharField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Materials list'

	def __str__(self) -> str:
		return f"{self.id} : {self.get_material_display()}"


class Gate(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	uuid = models.UUIDField(default = uuid.uuid4)
	last_update = models.DateTimeField(auto_now=True)
	last_update_by = models.CharField(blank=True, null=True)
	name = models.CharField()
	notes = models.CharField(blank=True, null=True)
	pic = models.ImageField(blank=True, null=True)
	geometry = models.PointField(blank=True, null=True)
	height_m = models.FloatField(blank=True, null=True)
	width_m = models.FloatField(blank=True, null=True)
	installation_date = models.DateTimeField(blank=True, null=True)
	is_date_estimated = models.BooleanField(blank=True, null=True)
	gate_direction_from_hinge_when_closed = models.FloatField(blank=True, null=True)
	gate_open_maximum_degrees = models.FloatField(blank=True, null=True)
	gate_open_minimum_degrees = models.FloatField(blank=True, null=True)
	gate_type_uuid = models.ForeignKey(
		GateType,
		models.DO_NOTHING,
		blank=True,
		null=True
	)
	gate_function_uuid = models.ForeignKey(
		GateFunction,
		models.DO_NOTHING,
		blank=True,
		null=True
	)

	def __str__(self) -> str:
		return f"{self.id} : {self.name}"

class GateMaterials(models.Model):
	id = models.PositiveIntegerField(primary_key=True) # need to figure out composite key: PRIMARY KEY (fk_gate_uuid, fk_gate_materials_uuid),
	uuid = models.UUIDField(default = uuid.uuid4)
	last_update = models.DateTimeField(auto_now=True)
	last_update_by = models.CharField(blank=True, null=True)
	name = models.CharField(blank=True, null=True)
	notes = models.CharField(blank=True, null=True)
	pic = models.ImageField(blank=True, null=True)
	gate_uuid = models.ForeignKey(
		Gate,
		models.DO_NOTHING,
		blank=True,
		null=True
	)
	gate_material_uuid = models.ForeignKey(
		GateMaterial,
		models.DO_NOTHING,
		blank=True,
		null=True
	)

	class Meta:
		verbose_name_plural = 'Gate Materials'

	def __str__(self) -> str:
		return f"{self.id} : {self.name}"

# class GateConditions(models.Model):
# 	id = models.PositiveIntegerField(primary_key=True) # need to figure out composite key: PRIMARY KEY (fk_gate_uuid, fk_gate_materials_uuid),
# 	gate_uuid = models.ForeignKey(
# 		Gate,
# 		models.DO_NOTHING,
# 		blank=True,
# 		null=True
# 	)
# 	condition_uuid = models.ForeignKey(
# 		Conditions,
# 		models.DO_NOTHING,
# 		blank=True,
# 		null=True
# 	)


	

# Create your models here.
