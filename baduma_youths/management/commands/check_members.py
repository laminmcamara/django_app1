from django.core.management.base import BaseCommand
from baduma_youths.models import Member
import uuid

class Command(BaseCommand):
    help = 'Check and fix UUIDs for members'

    def handle(self, *args, **kwargs):
        members = Member.objects.all()
        for member in members:
            print(f'ID: {member.id}, Full Name: {member.full_name}')
            if not isinstance(member.id, uuid.UUID):
                member.id = uuid.uuid4()  # Generate a new valid UUID
                member.save()
                print(f'Updated ID for {member.full_name} to {member.id}')


