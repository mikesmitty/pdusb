import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import ENTITY_CATEGORY_DIAGNOSTIC
from . import (
    CONF_MPQ4242_ID,
    MPQ4242Component,
)

CODEOWNERS = ["@mikesmitty"]

DEPENDENCIES = ["mpq4242"]

CONF_CABLE_5A_CAPABLE = "cable_5a_capable"
CONF_CURRENT_MISMATCH = "current_mismatch"
CONF_GIVEBACK_FLAG = "giveback_flag"
CONF_OVERHEAT_THRESHOLD_1 = "overheat_threshold_1"
CONF_OVERHEAT_THRESHOLD_2 = "overheat_threshold_2"
CONF_PPS_MODE = "pps_mode"
CONF_SINK_ATTACHED = "sink_attached"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_MPQ4242_ID): cv.use_id(MPQ4242Component),
    cv.Optional(CONF_CABLE_5A_CAPABLE): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_CURRENT_MISMATCH): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_GIVEBACK_FLAG): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_OVERHEAT_THRESHOLD_1): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_OVERHEAT_THRESHOLD_2): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_PPS_MODE): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    cv.Optional(CONF_SINK_ATTACHED): binary_sensor.binary_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
}


async def to_code(config):
    mpq4242_component = await cg.get_variable(config[CONF_MPQ4242_ID])
    if cable_5a_capable_config := config.get(CONF_CABLE_5A_CAPABLE):
        sens = await binary_sensor.new_binary_sensor(cable_5a_capable_config)
        cg.add(mpq4242_component.set_cable_5a_capable_binary_sensor(sens))

    if current_mismatch_config := config.get(CONF_CURRENT_MISMATCH):
        sens = await binary_sensor.new_binary_sensor(current_mismatch_config)
        cg.add(mpq4242_component.set_current_mismatch_binary_sensor(sens))

    if giveback_flag_config := config.get(CONF_GIVEBACK_FLAG):
        sens = await binary_sensor.new_binary_sensor(giveback_flag_config)
        cg.add(mpq4242_component.set_giveback_flag_binary_sensor(sens))

    if overheat_threshold_1_config := config.get(CONF_OVERHEAT_THRESHOLD_1):
        sens = await binary_sensor.new_binary_sensor(overheat_threshold_1_config)
        cg.add(mpq4242_component.set_overheat_threshold_1_binary_sensor(sens))

    if overheat_threshold_2_config := config.get(CONF_OVERHEAT_THRESHOLD_2):
        sens = await binary_sensor.new_binary_sensor(overheat_threshold_2_config)
        cg.add(mpq4242_component.set_overheat_threshold_2_binary_sensor(sens))

    if pps_mode_config := config.get(CONF_PPS_MODE):
        sens = await binary_sensor.new_binary_sensor(pps_mode_config)
        cg.add(mpq4242_component.set_pps_mode_binary_sensor(sens))

    if sink_attached_config := config.get(CONF_SINK_ATTACHED):
        sens = await binary_sensor.new_binary_sensor(sink_attached_config)
        cg.add(mpq4242_component.set_sink_attached_binary_sensor(sens))
