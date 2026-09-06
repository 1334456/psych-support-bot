from psych_support_bot.ai.routers.intent import detect_conversation_intent


def test_follow_up_intent() -> None:
    history = [{"role": "user", "content": "解释一下缓存命中率"}]
    assert detect_conversation_intent("那为什么还是很低？", history) == "follow_up"


def test_add_constraint_intent() -> None:
    history = [{"role": "user", "content": "帮我设计一个客服 Prompt"}]
    assert detect_conversation_intent("不能编造信息。", history) == "add_constraint"


def test_topic_switch_intent() -> None:
    history = [{"role": "user", "content": "帮我优化客服 Prompt"}]
    assert detect_conversation_intent("顺便帮我查一下订单状态。", history) == "topic_switch"


def test_clarification_needed_without_history() -> None:
    assert (
        detect_conversation_intent("继续处理刚才那个。", [])
        == "clarification_needed"
    )
