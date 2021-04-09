from rest_framework import serializers
from .models import Animal, Lot, Bid


class AnimalGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'type', 'breed', 'owner']


class AnimalSerializer(AnimalGetSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class LotGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ['id', 'animal', 'price', 'owner', 'winner_id']


class LotSerializer(LotGetSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class LotPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ['id', 'winner_id']


class BidGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'lot', 'value', 'owner']

    def get_queryset(self):
        lot_id = self.request.query_params.get('lot_id')
        queryset = Bid.objects.filter(lot__id=lot_id)
        return queryset


class BidSerializer(BidGetSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        # can't allow users to make bids on their own lots
        # if data['lot'].owner == data['owner']:
        #     raise serializers.ValidationError("You can't make a bid on your own lot.")
        # bid value must be higher than the base price
        if data['value'] < data['lot'].price:
            raise serializers.ValidationError("Your bid must be higher than the price")
        return data
